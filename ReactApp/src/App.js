import "./App.css";
import APIService from "./APIService";

function App() {
	/**
	 *  event on submit to sand request to API
	 * @param {import("react").FormEvent} eventSubmit 
	 */
	function handleOnSubmit(eventSubmit) {
		eventSubmit.preventDefault();
		APIService.sendData({
			'age': eventSubmit.target.user_age.value,
			'sex': eventSubmit.target.user_sex.value,
			'child': eventSubmit.target.user_hasChild.value
		});
	}

	return (
		<div className="App">
			<header className="App-header">
				<h1>Vérification bancaire</h1>
			</header>
			<div className="App-body">
				<form
					id="BankForm"
					onSubmit={(submitEvent) => {
						handleOnSubmit(submitEvent);
					}}>
					<div>
						<p>Age</p>
						<input
							type={"number"}
							id={"user_age"}
							min={"12"}
							max={"150"}
							defaultValue={"20"}
						/>
					</div>
					<div>
						<p>Sex</p>
						<select
							id="user_sex">
							<option id="sex_h" value="male" >Homme</option>
							<option id="sex_f" value="female" >Femme</option>
						</select>
					</div>
					<div>
						<p>Enfant ?</p>
						<input
							type={"checkbox"}
							id={"user_hasChild"}
						/>
					</div>
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