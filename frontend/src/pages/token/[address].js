import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import TokenHeader from '../../components/Token/TokenHeader'
import TokenChart from '../../components/Token/TokenChart'
import TokenInfo from '../../components/Token/TokenInfo'
import TokenSocial from '../../components/Token/TokenSocial'
import PostFeed from '../../components/Feed/PostFeed'
import { Web3 } from '@solana/web3.js';
const { Connection } = Web3;

export default function TokenPage() {
  const router = useRouter()
  const { address } = router.query
  const [tokenData, setTokenData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (address) {
      fetchTokenData()
    }
  }, [address])

  const fetchTokenData = async () => {
    try {
      const response = await fetch(`/api/tokens/${address}`)
      const data = await response.json()
      setTokenData(data)
    } catch (error) {
      console.error('Error fetching token data:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div>Loading token data...</div>
  }

  if (!tokenData) {
    return <div>Token not found</div>
  }

  return (
    <div className="token-page">
      <TokenHeader token={tokenData} />
      
      <div className="token-layout">
        <div className="token-main">
          <TokenChart tokenAddress={tokenData.contract_address} />
          <PostFeed tokenAddress={address} />
        </div>
        
        <div className="token-sidebar">
          <TokenInfo token={tokenData} />
          <TokenSocial token={tokenData} />
        </div>
      </div>

      <style jsx>{`
        .token-page {
          max-width: 1200px;
          margin: 0 auto;
          padding: 1rem;
        }
        .token-layout {
          display: grid;
          grid-template-columns: 2fr 1fr;
          gap: 2rem;
          margin-top: 2rem;
        }
        @media (max-width: 768px) {
          .token-layout {
            grid-template-columns: 1fr;
          }
        }
      `}</style>
    </div>
  )
}