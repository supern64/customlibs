// You must have https://github.com/Olical/EventEmitter on your website for this client to work

// Enumerations
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
window.WSCloseReason = {
  NORMAL: 1000,
  GOING_AWAY: 1001,
  PROTOCOL_ERROR: 1002,
  UNPROCESSABLE_INPUT: 1003,
  RESERVED: 1004,
  NOT_PROVIDED: 1005,
  ABNORMAL: 1006,
  INVALID_DATA: 1007,
  POLICY_VIOLATION: 1008,
  MESSAGE_TOO_BIG: 1009,
  EXTENSION_REQUIRED: 1010,
  INTERNAL_SERVER_ERROR: 1011,
  SERVICE_RESTART: 1012,
  TRY_AGAIN_LATER: 1013,
  BAD_GATEWAY: 1014,
  TLS_HANDSHAKE_FAILED: 1015
}
window.WSCloseDescription = {
  1000: 'Normal connection closure',
  1001: 'Remote peer is going away',
  1002: 'Protocol error',
  1003: 'Unprocessable input',
  1004: 'Reserved',
  1005: 'Reason not provided',
  1006: 'Abnormal closure, no further detail available',
  1007: 'Invalid data received',
  1008: 'Policy violation',
  1009: 'Message too big',
  1010: 'Extension requested by client is required',
  1011: 'Internal Server Error',
  1012: 'Service Restart',
  1013: 'Try Again Later',
  1014: 'Bad Gateway',
  1015: 'TLS Handshake Failed' 
}
Object.freeze(window.WSState)
Object.freeze(window.WSStateMap)
Object.freeze(window.WSCloseReason)
Object.freeze(window.WSCloseDescription)
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
      this.emit('close', event.code, event.reason, event)
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
      this._client.close(code, WSCloseDescription[code])
      return
    } else if (reason && !code) {
      throw new Error("Cannot close WebSocket w/ reason but w-o/ code")
    } else {
      this._client.close()
    }
  }
}
