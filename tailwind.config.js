/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./website/templates/**/*.{html,js}"
  ],
  theme: {
    backgroundColor: {
      'primary': '#FBDAD3',
      'secondary': '#E9635E',
      'azul-detalhe': '#52BDC3',
      'nuvem': '#F6F6F6',
      'white': '#FFFFFF',
    },
    textColor: {
      'primary': '#FBDAD3',
      'secondary': '#E63946',
      'azul-detalhe': '#52BDC3',
      'black': '#000000',
      'nuvem': '#F6F6F6',
      'DEFAULT': '#000000',
      'red': '#E63946',
    },
    borderColor: {
      'primary': '#FBDAD3',
      'secondary': '#E63946',
      'azul-detalhe': '#52BDC3',
      'nuvem': '#F6F6F6',
      'white': '#FFFFFF',
    },
    extend: {
      fontFamily: {
        'sans': ['Titillium Web', 'sans-serif'],
      },
      fontSize: {
        'base': '24px',
      },
    },
  },
  plugins: [],
}

