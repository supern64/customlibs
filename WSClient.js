// You must have https://github.com/Olical/EventEmitter on your website for this client to work
window.WSState = {
  CONNECTING: 0,
  OPEN: 1,
  CLOSING: 2,
  CLOSED: 3
}
window.WSStateMap = {
  0: "CONNECTING",
  1: "OPEN",
  2: "CLOSING",
  3: "CLOSED"
}
Object.freeze(window.WSState)
Object.freeze(window.WSStateMap)
function getStateFromNumber(num) { return WSStateMap[num] }

class WSClient extends EventEmitter {
  // Use this._client.bufferedAmount for buffered amount as it requires updating often
  constructor(url) {
    super()
    this._client = new WebSocket(url)
    this.url = this._client.url
    this.readyState = this._client.readyState
    this.readyStateEnum = getStateFromNumber(this._client.readyState)
    this.extensions = this._client.extensions
    this.binaryType = this._client.binaryType
    this._client.addEventListener('open', (event) => {
      this.emit('open', event)
      this.readyState = this._client.readyState
      this.readyStateEnum = getStateFromNumber(this._client.readyState)
    })
    this._client.addEventListener('message', (event) => {
      this.emit('message', event.data, event)
    })
    this._client.addEventListener('error', (event) => {
      this.emit('error', event.error, event)
      this.readyState = this._client.readyState
      this.readyStateEnum = getStateFromNumber(this._client.readyState)
    })
    this._client.addEventListener('close', (event) => {
      this.emit('close', event)
      this.readyState = this._client.readyState
      this.readyStateEnum = getStateFromNumber(this._client.readyState)
    })
    return this
  }
  send(data) {
    this._client.send(data)
    this.emit("send")
    return
  }
  close(code=null, reason=null) {
    if (code && reason) {
      this._client.close(code, reason)
      return
    } else if (code && !reason) {
      this._client.close(code)
      return
    } else if (reason && !code) {
      throw new Error("Cannot close WebSocket w/ reason but w-o/ code")
    } else {
      this._client.close()
    }
  }
}
