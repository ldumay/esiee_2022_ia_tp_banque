export default class APIService {

	static url = "http://localhost"
	static port = 5000

	/**
	 * Send data
	 * @param {*} body 
	 * @returns 
	 */
	static sendData(body) {
		let result = "";
		let url = new URL(this.url + ":" + this.port + "/bank")
		fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': "*",
				// 'Access-Control-Allow-Credentials' : true
			},
			body: JSON.stringify(body)
		}).then((response) => {
			response.json().then((jsonValue) => {
				console.debug(jsonValue);
				result = jsonValue;
			})
		}, (rejectMessage) => {
			console.log("Request rejected", rejectMessage)
		}).catch((error) => {
			console.err("Request Error", error)
		}).finally(() => {
			console.log("Request finish");
		});
		return result;
	}
}