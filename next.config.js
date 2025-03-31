module.exports = {
  reactStrictMode: true,
  images: {
    domains: ['assets.dexscreener.com'],
  },
  webpack: (config) => {
    config.resolve.fallback = { fs: false, net: false, tls: false }
    return config
  }
}