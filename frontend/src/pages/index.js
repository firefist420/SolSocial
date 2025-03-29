import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import { useWallet } from '@solana/wallet-adapter-react'
import HCaptcha from '@hcaptcha/react-hcaptcha'
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui'

export default function Home() {
  const { connected } = useWallet()
  const [captchaVerified, setCaptchaVerified] = useState(false)
  const router = useRouter()

  useEffect(() => {
    if (connected && captchaVerified) {
      router.push('/feed')
    }
  }, [connected, captchaVerified])

  return (
    <div className="min-h-screen flex items-center justify-center bg-cover bg-center" style={{backgroundImage: "url('/images/background.jpg')"}}>
      <div className="bg-black bg-opacity-80 p-8 rounded-xl text-center max-w-md w-full">
        <h1 className="text-3xl font-bold mb-6">Welcome to SolSocial</h1>
        <HCaptcha sitekey={process.env.NEXT_PUBLIC_HCAPTCHA_SITEKEY} onVerify={() => setCaptchaVerified(true)} />
        {captchaVerified && <WalletMultiButton className="mt-4 mx-auto" />}
      </div>
    </div>
  )
}