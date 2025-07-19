# 📹 Video Conferencing Clone (Python + Flask + VidStream)

A simple peer-to-peer video conferencing system using Flask for UI and `vidstream` for media streaming, including audio, video, and screen sharing.

# ✅ Features

- 🎥 Real-time camera video streaming
- 🖥️ Live screen sharing
- 🎙️ Audio streaming (send & receive)
- 🔁 Bi-directional streaming (Client ↔ Server)
- 🖱️ Easy-to-use Tkinter GUI for client/server
- 🌐 Web interface using Flask


# 📁 Project Structure

video-conferencing-clone/
├── app.py           # Flask app with routes
├── client.py        # Client-side streaming logic with GUI
├── server.py        # Server-side streaming logic with GUI
├── README.md        # Project documentation


# 🧰 Tech Stack

- "Python"
- "Flask" – for simple web server and navigation
- "Tkinter" – for client/server GUI
- "VidStream" – for video/audio/screen transmission
- "Socket & Threading" – for IP setup and concurrency


# 🚀 How to Run the Project

# 📌 Prerequisites

- Python 3.x
- Install required libraries:
  ```bash
  pip install flask vidstream

# ▶️ Start Flask App

``bash
python app.py

# 🌐 Open in Browser

* Navigate to `http://localhost:5000`
* Click on:

  * "Connect as Client" – to open the client GUI
  * "Connect as Server" – to open the server GUI

---

# 🎛️ Functional Buttons (in GUI)

**In both Client and Server GUIs:**

* 🔊 **Start Audio Stream**
* 🎥 **Start Camera Stream**
* 🖥️ **Start Screen Sharing**
* 📡 **Start Listening** (to receive streams)

---

## 🧠 How It Works

* Flask serves a landing page with links to run either `client.py` or `server.py`.
* The Tkinter GUI allows entering a target IP and selecting the desired stream type.
* `vidstream` handles all the encoding and real-time media transmission using socket-based connections.

---

## 🔒 Notes

* Run both client and server on the same network (LAN or localhost).
* Ensure firewall allows streaming ports (default: 6666, 7777, 8888, 9999).
* Works best on Windows (due to `os.system()` used in `app.py`).

---

## 🛠️ To Improve

* Add secure connection support (SSL/TLS)
* Add chat messaging feature
* Enable multi-user conferencing with room IDs
* Switch to `subprocess` for better cross-platform compatibility

---

## 🤝 Contribution

Pull requests and suggestions are welcome! Please fork the repo and submit your ideas.

---

## 📧 Contact

* Created by: "Aditya Kumar"
* LinkedIn: https://www.linkedin.com/in/aditya-kumar-95716a256/
* GitHub: https://www.linkedin.com/in/aditya-kumar-95716a256/
