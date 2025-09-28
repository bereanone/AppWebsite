export default {
  theme: {
    extend: {
      colors: {
        parchment: '#fdf6e3',
        sepia: '#1a0e0e',
        verse: '#5a4a3b',
        accent: '#e6ddc4',
        accentHover: '#dcd2b8',
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', 'Times New Roman', 'serif'],
      },
    },
  },
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  plugins: [],
}