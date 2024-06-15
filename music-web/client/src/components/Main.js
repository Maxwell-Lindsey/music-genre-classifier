import React from "react";
import styles from "../styles/Main.module.css";

const Main = () => {
  const uploadFile = async (e) => {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("http://localhost:5000/upload_file", {
        method: "post",
        body: data,
      });

      let res = await response.json();
      if (res.status !== 1) {
        console.log("Error uploading file");
      }
    }
  };

  return (
    <form>
      <h1>Music </h1>
      <input type="file" onChange={uploadFile}></input>
      <button className="btn">Button</button>
    </form>
  );
};

export default Main;
