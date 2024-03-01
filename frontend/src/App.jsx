// Built in packages
import { useState, useEffect } from "react";
import axios from "axios";

// CSS
import "./App.css";

function App() {
  // States
  const [serverResp, setServerResp] = useState("Not Connected");

  useEffect(() => {
    fetchSampleResp();
  }, []);

  // Handlers
  const fetchSampleResp = async () => {
    const resp = await axios.get(
      import.meta.env.VITE_CHAIN_MAKER_BACKEND_URL + "/healthcheck"
    );

    setServerResp(resp.data);
  };

  return (
    <>
      <div>
        <h1>Chain Maker</h1>
      </div>
      <h6>
        Server Status: <b>{serverResp}</b>
      </h6>
    </>
  );
}

export default App;
