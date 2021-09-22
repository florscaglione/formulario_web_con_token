import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.scss";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const url = "https://3001-pink-lobster-5042dndp.ws-eu17.gitpod.io/";

	fetch(`${url}api/countries/create`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({
			name: "Prueba7"
		})
	}).then(response => console.log(response));

	fetch(`${url}api/countries/1/cities/create`, {
		method: "POST",
		body: JSON.stringify({
			name: "CiudadPrueba7"
		}),
		headers: {
			"Content-Type": "application/json"
		}
	}).then(response => console.log(response));

	fetch(`${url}api/users/create`, {
		method: "POST",
		body: JSON.stringify({
			email: "Prueba7@gmail.com",
			password: "password"
		}),
		headers: {
			"Content-Type": "application/json"
		}
	}).then(response => console.log(response));

	fetch(`${url}api/users/create`, {
		method: "POST",
		body: JSON.stringify({
			email: "email_with_city7@gmail.com",
			password: "password",
			city_id: 5
		}),
		headers: {
			"Content-Type": "application/json"
		}
	}).then(response => console.log(response));

	/* async function loadUser() {
		const user = await fetch(`https://3001-cyan-galliform-3nlrp71m.ws-eu16.gitpod.io/api/user/1/`).then(response =>
			response.json()
		);
		const city = await fetch(
			`https://3001-cyan-galliform-3nlrp71m.ws-eu16.gitpod.io/api/cities/${user.city_id}/`
		).then(response => response.json());
		const country = await fetch(
			`https://3001-cyan-galliform-3nlrp71m.ws-eu16.gitpod.io/api/cities/${user.country_id}/`
		).then(response => response.json());
		user.city = city;
		user.city.country = country;
		console.log(user);
		//setUser(user);
	} */

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!</h1>
			<p>
				<img src={rigoImageUrl} />
			</p>
			<div className="alert alert-info">{store.message || "Loading message from the backend..."}</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://github.com/4GeeksAcademy/react-flask-hello/tree/95e0540bd1422249c3004f149825285118594325/docs">
					Read documentation
				</a>
			</p>
		</div>
	);
};
