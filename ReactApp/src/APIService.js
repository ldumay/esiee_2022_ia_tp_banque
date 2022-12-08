export default class APIService {

	url = "http://localhost"
	port = 5000

	/**
	 * Send data
	 * @param {*} body 
	 * @returns 
	 */
	static sendData(body) {
		let result = "";
		fetch(this.url + ":" + this.port + "/test",
			{
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					// 'Access-Control-Allow-Origin' : 'http://192.168.1.24:3000',
					// 'Access-Control-Allow-Credentials' : true
				},
				body: JSON.stringify(body)
			})
			.then((response) => {
				response.json().then((jsonValue) => {
					console.debug(jsonValue);
					result = jsonValue;
				})
			}, (rejectMessage) => {
				console.log(rejectMessage)
			}).catch((error) => {
				console.err(error)
			}).finally(() => {
			});
		return result;
	}
}