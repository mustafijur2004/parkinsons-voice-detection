import { Link, Route, Routes } from 'react-router-dom'

import AdminDashboard from './pages/AdminDashboard'
import DoctorDashboard from './pages/DoctorDashboard'
import Login from './pages/Login'
import UserDashboard from './pages/UserDashboard'

function App() {
  return (
    <div className="app-shell">
      <header className="site-header">
        <h1>Parkinson&apos;s Voice Detection</h1>
        <nav aria-label="Primary navigation">
          <Link to="/login">Login</Link>
          <Link to="/user">User</Link>
          <Link to="/doctor">Doctor</Link>
          <Link to="/admin">Admin</Link>
        </nav>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/user" element={<UserDashboard />} />
          <Route path="/doctor" element={<DoctorDashboard />} />
          <Route path="/admin" element={<AdminDashboard />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
