import { useWallet } from '@solana/wallet-adapter-react';
import HCaptcha from '@hcaptcha/react-hcaptcha';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

export default function Home() {
  const { connected } = useWallet();
  const [captchaVerified, setCaptchaVerified] = useState(false);
  const router = useRouter();

  useEffect(() => {
    if (connected && captchaVerified) {
      router.push('/feed');
    }
  }, [connected, captchaVerified, router]);

  return (
    <div className="welcome-container">
      <div className="welcome-content">
        <h1>Welcome to SolSocial</h1>
        <HCaptcha
          sitekey={process.env.NEXT_PUBLIC_HCAPTCHA_SITEKEY}
          onVerify={() => setCaptchaVerified(true)}
        />
        {captchaVerified && (
          <WalletMultiButton className="connect-button" />
        )}
      </div>
      <style jsx>{`
        .welcome-container {
          background-image: url('/images/background.jpg');
          background-size: cover;
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .welcome-content {
          background: rgba(0, 0, 0, 0.8);
          padding: 2rem;
          border-radius: 1rem;
          text-align: center;
          max-width: 500px;
          width: 100%;
        }
      `}</style>
    </div>
  );
}