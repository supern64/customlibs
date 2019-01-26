// A very simple and tiny wrapper around speechSynthesis
const synth = window.speechSynthesis
if (!synth) throw new Error("Your browser does not support the Speech Synthesis API. Chrome 33 and newer is required.")
function speak(text) {
  var utter = new SpeechSynthesisUtterance(text)
  synth.speak(utter)
}
