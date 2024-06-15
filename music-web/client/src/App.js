import "./App.css";
import styles from "./styles/App.module.css";
import { useState, useEffect } from "react";
// import pink from "../../flask-server/uploads/PinkPanther30.wav";

function App() {
  const [file, setFile] = useState(null);
  const [audio, setAudio] = useState(null);
  const [genre, setGenre] = useState("");
  const [theme, setTheme] = useState("light");

  function handleAudioPlay() {
    var AudioPlay = new Audio(file);
    setAudio(AudioPlay);
    AudioPlay.play()
      .then(() => {
        // Audio is playing.
      })
      .catch((error) => {
        console.log(error);
      });
  }

  function handleAudioStop() {
    audio.pause();
  }

  const toggleTheme = () => {
    if (theme === "light") {
      setTheme("dark");
    } else {
      setTheme("light");
    }
  };
  useEffect(() => {
    document.body.className = theme;
  }, [theme]);


  const uploadFile = async (e) => {
    // e.preventDefault();
    const file = e.target.files[0];
    if (file != null) {
      // check length
      // if (file.size > 10000000) {

      // var AudioPlay = new Audio(file);
      // AudioPlay.play();
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("http://localhost:5000/upload_file", {
        method: "post",
        body: data,
      });
      let res = await response.json();
      // if (res.status !== 1) {
      //   alert("Error uploading file");
      // }
      console.log(res);
      setFile(URL.createObjectURL(e.target.files[0]));
      console.log(file);
      setGenre(res["result"]);
    }
  };

  function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  // const uploadFile = async (e) => {
  //   e.preventDefault();
  //   // console.log(file);
  //   // const formData = new FormData();

  //   // formData.append("file", file);

  //   // await fetch("http://localhost:5000/upload_file", {
  //   //   method: "POST",
  //   //   body: formData,
  //   //   headers: {
  //   //     "Content-Type": "multipart/form-data",
  //   //   },
  //   // }).then((response) => {
  //   //   console.log(response);
  //   // });
  //   // await fetch("http://localhost:5000/upload_file", {
  //   //   method: "POST",
  //   //   body: formData,
  //   //   // method: "POST",
  //   //   headers: {
  //   //     "Content-Type": "multipart/form-data",
  //   //   },
  //   // })
  //   //   .then((response) => response.json())
  //   //   .then((result) => {
  //   //     console.log("Success:", result);
  //   //   })
  //   //   .catch((error) => {
  //   //     console.error("Error:", error);
  //   //   });
  //   // console.log("Clicked");
  //   // // const file = e.target.files[0];
  //   // console.log(e.target.file);
  //   if (file != null) {
  //     const data = new FormData();
  //     data.append("file_from_react", file);
  //     // enctype = multipart / form - data;
  //     let response = await fetch("http://localhost:5000/upload_file", {
  //       method: "post",
  //       body: data,
  //       headers: {
  //         "Content-Type": "multipart/form-data",
  //       },
  //     });

  //     let res = await response.json();
  //     if (res.status !== 1) {
  //       console.log("Error uploading file");
  //     }
  //   }
  // };

  return (
    <div className={styles[theme]}>
    <div className={styles.container}>
      <form className={styles.form}>
        <h1 className={`${styles.header} text-5xl font-bold`}>
          Music Genre Classifier
        </h1>
        
        <span class="inline-block animate-spin">
          <div className={styles.avatar}>
            <div class="w-24 rounded">
              <img src="https://www.freeiconspng.com/uploads/light-blue-music-note-picture-15.png" />
            </div>
          </div>
        </span>
      </form>
      {/* <h1 className="text-5xl font-bold">Music Genre Classifier</h1> */}
      <div className={styles.utilityBar}>
      <p>Upload an audio file and see what the genre is.</p>
          <button className="btn" onClick={toggleTheme}>
            Switch to {theme == "dark" ? "light" : " dark"} mode
          </button>
      </div>
      <div className={`${styles.warning} alert alert-info shadow-lg`}>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="stroke-current flex-shrink-0 w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
          <span>You may only upload .mp3 and .wav files.</span>
        </div>
      </div>
      <div className={styles.badgeWrapper}>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          blues
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          classical
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          country
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          disco
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          hiphop
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          jazz
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          metal
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          pop
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          reggae
        </div>
        </span>
        <span class="inline-block animate-bounce">
        <div
          style={{ backgroundColor: getRandomColor() }}
          className="badge badge-lg"
        >
          rock
        </div>
        </span>
      </div>
      <form className={styles.form}>
        <input onChange={uploadFile} type="file" accept=".mp3,.wav"></input>

        <label for="my-modal" class="btn">
          View Results
        </label>
        {/* <button className="btn">View Results</button> */}
        <input type="checkbox" id="my-modal" className="modal-toggle" />
        <div className="modal">
          <div className="modal-box w-11/12 max-w-5xl">
            <p className="py-4">Genre: "{genre}".</p>
            <div
              onClick={handleAudioPlay}
              className="btn backdrop:btn-sm btn-success"
            >
              Play Audio
            </div>
            <div onClick={handleAudioStop} className="modal-action">
              <label htmlFor="my-modal" className="btn">
                Yay!
              </label>
            </div>
          </div>
        </div>
      </form>
      {/* <h1>Genre: {genre}</h1> */}
      {/* <button onClick={handleClick} className="btn">
        Upload
      </button> */}
      {/* <br />
      <br />
      <br />
      <br />
      <br /> <br /> <br />
      <br />
      <br />
      <br /> */}
      {/* <div class="avatar-group -space-x-6">
        <div class="avatar">
          <div class="w-12">
            <img src="https://canvas.illinois.edu/images/thumbnails/5557236/TSSHozO2UuzaG5XQqBHQoZBgmc2TDaSex4RvYGjD" />
          </div>
        </div>
        <div class="avatar">
          <div class="w-12">
            <img src="https://canvas.illinois.edu/images/thumbnails/5725397/DplRsnCFyu8ucKAnv6ngMZbCILvzX6xT74HjNh1M" />
          </div>
        </div>
        <div class="avatar">
          <div class="w-12">
            <img src="https://canvas.illinois.edu/images/thumbnails/5625870/vM7bPiajUwVZhlLp7fS88wJEM5XAZ2uaWsl26tIB" />
          </div>
        </div>
        <div class="avatar">
          <div class="w-12">
            <img src="https://canvas.illinois.edu/images/thumbnails/5738960/Cb35NY02lYzDF5x1g7Jg8sQfqKWVzuiMwkDBZgnN" />
          </div>
        </div>
      </div> */}
      <img src="https://media.tenor.com/SbM_HDQqUtgAAAAC/bongo-cat-playing.gif" />
      <footer class="footer footer-center items-center p-4 bg-neutral text-neutral-content">
        <div class="avatar-group -space-x-6">
          <div class="avatar">
            <div class="w-12">
              <img src="https://canvas.illinois.edu/images/thumbnails/5557236/TSSHozO2UuzaG5XQqBHQoZBgmc2TDaSex4RvYGjD" />
            </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://canvas.illinois.edu/images/thumbnails/5725397/DplRsnCFyu8ucKAnv6ngMZbCILvzX6xT74HjNh1M" />
            </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://canvas.illinois.edu/images/thumbnails/5625870/vM7bPiajUwVZhlLp7fS88wJEM5XAZ2uaWsl26tIB" />
            </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://canvas.illinois.edu/images/thumbnails/5738960/Cb35NY02lYzDF5x1g7Jg8sQfqKWVzuiMwkDBZgnN" />
            </div>
          </div>
        </div>
        <div class="items-center grid-flow-col">
          <svg
            width="36"
            height="36"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            fill-rule="evenodd"
            clip-rule="evenodd"
            class="fill-current"
          >
            <path d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
          </svg>
          <p>
            Developed by: Jacob Chang, Max Lindsey, Daniel Murphy, David Sohn
          </p>
        </div>
        {/* <div class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
          <a>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              class="fill-current"
            >
              <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
            </svg>
          </a>
          <a>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              class="fill-current"
            >
              <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
            </svg>
          </a>
          <a>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              class="fill-current"
            >
              <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
            </svg>
          </a>
        </div> */}
      </footer>
    </div>
    </div>
  );
}

export default App;
