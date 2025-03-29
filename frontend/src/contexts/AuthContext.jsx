import { createContext, useContext } from 'react'
import { useWallet } from '@solana/wallet-adapter-react'

const AuthContext = createContext()

export function AuthProvider({ children }) {
  const wallet = useWallet()

  return (
    <AuthContext.Provider value={wallet}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}