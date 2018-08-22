// import 'react-hot-loader/path';
require("react-hot-loader/patch")
import ReactDOM from'react-dom';
import React from 'react';
import Greeting from './greeting';
import { AppContainer } from 'react-hot-loader';


const renderApp = Component => {
	ReactDOM.render(
		<AppContainer>
			<Component />
		</AppContainer>,
		document.getElementById('magic_act')
	)
}

renderApp(Greeting)


if (module.hot) {
	module.hot.accept();
}