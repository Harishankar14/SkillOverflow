<script setup>
    import Nav_Bar from './Nav_Bar.vue'
</script>


<template>
    <div class="meet-container">
        <Nav_Bar @custom-leave-event="handleleaveEvent"></Nav_Bar>
        <div>
        <iframe
             src="https://spatikam.whereby.com/spatikama712d3cf-2938-41ac-a34f-e970b94694b5"
             allow="camera; microphone; speaker; fullscreen; display-capture">
        </iframe>
        </div>

        
    </div>
</template>

<style>
    .meet-container{
        display: flex;
        flex-direction: row;
        top: 0;
        left: 0;
        position: fixed;
        width: 100%;
        height: 100%;
    }
    iframe{
        margin-top: 5%;
        height: 90%;
        width: 100%;
        position: fixed;
    }
</style>

<script>
    export default{
        methods:{
            handleleaveEvent(data){
                this.$emit('custom-leave-event', data);
                console.log(data)
            }
        }
    }
</script>


<!--<script setup>
    import {intializeApp} from 'firebase/app';
    import {getFirestore} from 'firebase/firestore';
    import {setupMedia} from './myscript.js';
    import {sendCandidate} from './myscript.js';
    import {listenForCandidates} from './myscript.js';
    import {sendOffer} from './myscript.js';
    import {listenForOffer} from './myscript.js';
    import {listenForAnswer} from './myscript.js';
    import {startConnection} from './myscript.js';
    import {hangup} from './myscript.js';
    import {startRecording} from './myscript.js';
    import {stopRecording} from './myscript.js';
</script>

<template>
    <div class="video-container">
        <h2>WebRTC Demo</h2>

    <h3>Initiate a Call</h3>
    <input id="receiverIdInput" placeholder="Enter Receiver's User ID" />
    <button id="initiateCallButton">Initiate Call</button>

    <h3>Wait for a Call</h3>
    <button id="waitForCallButton">Wait for Call</button>

    <h3>Video Streams</h3>
    <div class="videos">
      <div>
        <h4>Local Stream</h4>
        <video id="webcamVideo" autoplay playsinline muted></video>
      </div>
      <div>
        <h4>Remote Stream</h4>
        <video id="remoteVideo" autoplay playsinline></video>
      </div>
    </div>

    <div>
      <button id="startRecordingButton">Start Recording</button>
      <button id="stopRecordingButton" disabled>Stop Recording</button>
      <button id="downloadButton" disabled>Download Recording</button>
    </div>

    <h3>Hangup</h3>
    <button id="hangupButton" disabled>Hangup</button>

    </div>

</template>


<script>
    
    export default{data() {
    return {
      receiverId: "",
      localStream: null,
      remoteStream: null,
      isOnCall: false,
      isRecording: false,
      mediaRecorder: null,
      recordedChunks: [],
      firebaseConfig: {
        // Add your Firebase config here
        apiKey: "AIzaSyDK0OZbGROxwjCcQ69PwxZmWYuUJadiXoQ",
        authDomain: "skills-ecec4.firebaseapp.com",
        projectId: "skills-ecec4",
        storageBucket: "skills-ecec4.firebasestorage.app",
        messagingSenderId: "676986571580",
        appId: "1:676986571580:web:5909dfbe306de8b8786c39",
        measurementId: "G-YWZG68BN4V",
      },
      pc: null,
      firestore: null, // Firestore instance
    };
  },
  mounted() {
    // Initialize Firebase
    const app = initializeApp(this.firebaseConfig);
    this.firestore = getFirestore(app);  // Initialize Firestore

    this.setupWebRTC();
  },
        methods:{
            setupMedia(){
                setupMedia();
            },
            sendCandidate(token,candiate){
                sendCandidate(token,candiate);
            },
            listenForCandidates(token){
                listenForCandidates(token);
            },
            sendOffer(token,offer){
                sendOffer(token,offer);
            },
            listenForOffer(token){
                listenForOffer(token);
            },
            listenForAnswer(token){
                listenForAnswer;
            },
            startConnection(isCaller,token){
                startConnection(isCaller,token);
            },
            hangup(){
                hangup();
            },
            startRecording(){
                startRecording();
            },
            stopRecording(){
                stopRecording();
            },
            run_program(){
                const firebaseConfig = { 
                    apiKey: "AIzaSyDK0OZbGROxwjCcQ69PwxZmWYuUJadiXoQ",
                    authDomain: "skills-ecec4.firebaseapp.com",
                    projectId: "skills-ecec4",
                    storageBucket: "skills-ecec4.firebasestorage.app",
                    messagingSenderId: "676986571580",
                    appId: "1:676986571580:web:5909dfbe306de8b8786c39",
                    measurementId: "G-YWZG68BN4V"
                };
                if (!firebase.apps.length) firebase.initializeApp(firebaseConfig);
                const firestore = firebase.firestore();

                const servers = { iceServers: [{ urls: ['stun:stun1.l.google.com:19302'] }] };
                const pc = new RTCPeerConnection(servers);
                let localStream = null;
                let remoteStream = null;

                // HTML Elements
                const webcamVideo = document.getElementById('webcamVideo');
                const remoteVideo = document.getElementById('remoteVideo');
                const receiverIdInput = document.getElementById('receiverIdInput');
                const initiateCallButton = document.getElementById('initiateCallButton');
                const waitForCallButton = document.getElementById('waitForCallButton');
                const hangupButton = document.getElementById('hangupButton');
                
                hangupButton.onclick = () => {
                hangup()
                };

                // Initiate a call
                initiateCallButton.onclick = async () => {
                const receiverId = receiverIdInput.value;
                if (!receiverId) return alert('Please enter a receiver ID.');

                const callDoc = firestore.collection('calls').doc();
                const token = callDoc.id;

                // Notify receiver via backend
                await fetch('https://kangaroo-witty-glowworm.ngrok-free.app/send-token', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json',
                    'ngrok-skip-browser-warning': '69420',
                    },
                    body: JSON.stringify({ token, receiver_id: receiverId }),
                });

                await setupMedia();
                await startConnection(true, token);
                hangupButton.disabled = false;
                };

                // Wait for a call
                waitForCallButton.onclick = async () => {
                await setupMedia();

                const receiverId = prompt('Enter your User ID to wait for calls:');
                if (!receiverId) return;

                try {
                    const response = await fetch(`https://kangaroo-witty-glowworm.ngrok-free.app/get-token/${receiverId}`, {
                    method: 'GET',
                    headers: {
                        'ngrok-skip-browser-warning': '69420',
                    }
                });
                    const data = await response.json(); // This might fail if the response isn't JSON
                    if (data.call_token) {
                    await startConnection(false, data.call_token);
                    hangupButton.disabled = false;
                    } else {
                    alert(data.error || 'No incoming calls.');
                    }
                } catch (error) {
                    console.error('Failed to fetch token:', error);
                    alert('Failed to fetch token. Check console for details.');
                }
                };

                // The following code is for recording and downloading remote streams.
                let mediaRecorder;
                let recordedChunks = [];

                // HTML Elements for recording controls
                const startRecordingButton = document.getElementById('startRecordingButton');
                const stopRecordingButton = document.getElementById('stopRecordingButton');
                // Attach event listeners to buttons
                startRecordingButton.onclick = startRecording;
                stopRecordingButton.onclick = stopRecording;
            }
            
        }
    }
</script>

<style scoped>
    .video-container{
        background-color: white;
        top: 0;
        left: 0;
        position: fixed;
        width: 100%;
        height: 100%;
        font-family: 'Syne Mono', monospace;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin: 80px 10px;
    }
    .video {
        width: 40vw;
        height: 30vw;
        margin: 2rem;
        background: #2c3e50;
    }

    .videos {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>-->