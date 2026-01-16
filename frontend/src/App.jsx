import { useState } from "react";
import api from "./api";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState(null);

  const login = async () => {
    const res = await api.post("/auth/login", {
      email,
      password,
    });
    localStorage.setItem("token", res.data.access_token);

    const me = await api.get("/users/me");
    setUser(me.data);
  };

  if (user) {
    return <h1>Welcome {user.email}</h1>;
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>SupportHub</h1>
      <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <br />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <br />
      <button onClick={login}>Login</button>
    </div>
  );
}

export default App;
