import "./App.css";
import APIService from "./APIService";

function App() {
	/**
	 *  event on submit to sand request to API
	 * @param {import("react").FormEvent} eventSubmit 
	 */
	function handleOnSubmit(eventSubmit) {
		eventSubmit.preventDefault();
		APIService.sendData(eventSubmit);
	}

	return (
		<div className="App">
			<header className="App-header">
				<h1>Vérfication bancaire</h1>
			</header>
			<div className="App-body">
				<form
					id="BankForm"
					onSubmit={(submitEvent) => {
						handleOnSubmit(submitEvent);
					}}>
					<input
						type={"number"}
						id={"data1"}
					/>
					<input
						type={"number"}
						id={"data2"}
					/>
					<input
						type={"number"}
						id={"data3"}
					/>
					<input
						id="buttonSubmit"
						type={"submit"}
						name={"Envoyer"}
					/>
				</form>
			</div>


		</div>
	);
}

export default App;