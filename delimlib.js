const isNode = typeof process !== 'undefined' && process.versions != null && process.versions.node != null;

export function parse(text, delimeter=":", newlineDelimeter="\n") {
    if (delimeter == newlineDelimeter) {
	throw new Error("Delimeter cannot be the same as newline delimeter")
    }
    var parseData = text.split(newlineDelimeter)
    var returnValue = {}
    for (var i in parseData) {
        var b = parseData[i].split(delimeter)
        returnValue[b[0].trim()] = b[1].trim()
    }
    return returnValue
}
export function construct(object, delimeter=": ", newlineDelimeter="\n") {
    if (delimeter == newlineDelimeter) {
	throw new Error("Delimeter cannot be the same as newline delimeter")
    }
    var array = []
    for (var key in object) {
        array.push(key + delimeter + object[key])
    }
    return array.join(newlineDelimeter)
}
if (isNode) {
    module.exports.parse = parse
    module.exports.construct = construct
}
