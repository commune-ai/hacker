
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import { getRepos } from '../lib/api'

export default function Home() {
  const [repos, setRepos] = useState([])

  useEffect(() => {
    async function fetchRepos() {
      const repoData = await getRepos()
      setRepos(repoData)
    }
    fetchRepos()
  }, [])

  return (
    <div className={styles.container}>
      <Head>
        <title>CollabCode</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to <a href="https://nextjs.org">CollabCode</a>
        </h1>

        <p className={styles.description}>
          Collaborate on code with ease
        </p>

        <div className={styles.grid}>
          {repos.map((repo) => (
            <Link href={`/repos/${repo.id}`} key={repo.id}>
              <a className={styles.card}>
                <h3>{repo.name} &rarr;</h3>
                <p>{repo.description}</p>
              </a>
            </Link>
          ))}
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <img src="/vercel.svg" alt="Vercel Logo" className={styles.logo} />
        </a>
      </footer>
    </div>
  )
}
