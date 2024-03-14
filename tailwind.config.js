/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      fontFamily: {
        'bitter': ["Bitter", "serif"],
        'ultra': ["Ultra", "serif"]
      },
      colors: {
        'dark': '#26252D',
      }
    },
  },
  plugins: [
    require('flowbite/plugin'),
  ]
}

