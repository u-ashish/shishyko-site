module.exports = {
    purge: [
      './_includes/**/*.html',
      './_layouts/**/*.html',
      './_posts/*.md',
      './*.html',
    ],
    darkMode: false,
    theme: {
      extend: {
        colors: {
          'shishyko-bg': '#1a232e',
          'shishyko-text': '#cdd7e3',
          'shishyko-link': '#A5AF9B',
        },
        fontFamily: {
          sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Helvetica', 'Arial', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji'],
        },
        maxWidth: {
          'prose': '35em',
        },
        fontSize: {
          'base': '16px',
          'lg': '1.4rem',
        },
        lineHeight: {
          'relaxed': '1.5em',
        },
      },
    },
    variants: {
      extend: {},
    },
    plugins: [],
  }

//   https://icolorpalette.com/color/pantone-19-4118-tpx