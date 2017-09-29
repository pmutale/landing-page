var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: './themes/react/app',

  output: {
      path: path.resolve('./static/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new BundleTracker({filename: 'webpack-stats.json'})
  ],

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
          exclude: /node_modules/,
          loader: 'babel-loader'
      }
    ]
  },

  resolve: {
    // modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx']
  }
};