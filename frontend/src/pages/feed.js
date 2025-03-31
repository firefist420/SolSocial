import { useState } from 'react'
import PostForm from '../components/Feed/PostForm'
import PostList from '../components/Feed/PostList'
import Navbar from '../components/UI/Navbar'
import { Web3 } from '@solana/web3.js';
const { Connection } = Web3;

export default function Feed() {
  const [posts, setPosts] = useState([])

  return (
    <div className="min-h-screen bg-gray-900">
      <Navbar />
      <div className="max-w-4xl mx-auto p-4">
        <PostForm setPosts={setPosts} />
        <PostList posts={posts} />
      </div>
    </div>
  )
}