const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
	context: __dirname,

	entry: [
		'webpack-dev-server/client?http://familie.landing.localhost:7070',
		'webpack/hot/only-dev-server',
		'../themes/react/app'
	],

	output: {
		path: path.resolve('../static/bundles/'),
		filename: '[name]-[hash].bundle.js',
		publicPath: '/static/bundles'
	},

	plugins: [
		new webpack.HotModuleReplacementPlugin(),
		new webpack.NamedModulesPlugin(),
		new BundleTracker({filename: 'webpack-stats.json'}),
		new webpack.optimize.OccurrenceOrderPlugin(),
		new CleanWebpackPlugin(['./static/bundles/']),
		// new HtmlWebpackPlugin ({
		// title: 'Output Management'
		// })
		
	],

	externals: [

	],

	// devtool: 'inline-source-map',
  
	devServer: {
		hot: true,
		inline: true,
		port: 7070,
		host:"familie.landing.localhost",
		proxy: {
			'**': 'http://localhost:7000'
		}
	},

	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: [
					{
						loader: 'babel-loader',
						query: {
							cacheDirectory: true
						}
					}
				],
			},

			{
				test: /\.jsx$/,
				exclude: /node_modules/,
				use: [
					{
						loader: 'eslint-loader',
						query: {
							cacheDirectory: true
						}
					}
				]
			},

			{
				test: /\.html$/,
				use: [{
					loader: 'html-loader'
				}]
			},
			
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [{
					loader: 'file-loader',
					query: '[name].[ext]'
				}]
			}
		]
	},

	resolve: {
		modules: [
			'node_modules', 'bower_components'
		],
		extensions: ['.js', '.jsx']
	}
};