var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: './main.js',
    output: {
        path: path.resolve('./static/javascripts/bundles/'),
        filename: 'app.js',
        publicPath: ''
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],

    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ],
    },
    resolve: {
        alias: {
          vue: 'vue/dist/vue.js',
        }
    },

};