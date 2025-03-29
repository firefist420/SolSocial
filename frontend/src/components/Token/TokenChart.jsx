export default function TokenChart({ tokenAddress }) {
  return (
    <div className="chart-container">
      <iframe 
        src={`https://dexscreener.com/solana/${tokenAddress}?embed=1&theme=dark`}
        width="100%"
        height="400"
        frameBorder="0"
      />
    </div>
  )
}