function Login() {
  return (
    <section className="page-card">
      <h2>Login</h2>
      <p>Authentication will be implemented here.</p>
      <form>
        <label>
          Email
          <input type="email" name="email" placeholder="you@example.com" />
        </label>
        <label>
          Password
          <input type="password" name="password" placeholder="Password" />
        </label>
        <button type="button">Sign in</button>
      </form>
    </section>
  )
}

export default Login
