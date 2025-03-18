/** @type {import('tailwindcss').Config} */
export default {
  content: ["./udo/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "homecolor": "#A1E3F9",
        "cgray": "#3A4750",
      },
    }
  },
  daisyui: {
    themes: [
      {
        mytheme: {

          "primary": "#211C1B", // bg

          "secondary": "#DDDCCE", // btn-bg

          "accent": "#CFBA8E", // keyword

          "neutral": "#FFFFFF", // white 

          "base-100": "#000000",

          "info": "#006CF7",

          "success": "#A8B4E1",

          "warning": "#00ff00",

          "error": "#DA5C53",
        },
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
}
