/** @type {import('tailwindcss').Config} */
export default {
  content: [
    '../**/*.{html,js,jsx,ts,tsx}', // Include all relevant file types
    '!../node_modules/**/*', // Exclude node_modules
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
    require("@tailwindcss/typography")
  ],
}
