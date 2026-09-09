'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import type { User } from '@supabase/supabase-js';
import { supabase } from './supabase';

const AuthContext = createContext<{ user: User | null }>({ user: null });
export const useAuth = () => useContext(AuthContext);

export function AuthGate({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(Boolean(supabase));
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mode, setMode] = useState<'signin' | 'signup'>('signin');
  const [message, setMessage] = useState('');
  const [working, setWorking] = useState(false);

  useEffect(() => {
    if (!supabase) return;
    supabase.auth.getUser().then(({ data }) => { setUser(data.user); setLoading(false); });
    const { data } = supabase.auth.onAuthStateChange((_event, session) => setUser(session?.user ?? null));
    return () => data.subscription.unsubscribe();
  }, []);

  async function submit(event: React.FormEvent) {
    event.preventDefault(); const client=supabase; if (!client) return;
    setWorking(true); setMessage('');
    const result = mode === 'signin'
      ? await client.auth.signInWithPassword({ email, password })
      : await client.auth.signUp({ email, password, options: { emailRedirectTo: window.location.origin } });
    setWorking(false);
    if (result.error) setMessage(result.error.message);
    else if (mode === 'signup' && !result.data.session) setMessage('Check your email to confirm your account.');
  }

  if (loading) return <main className="auth-screen"><div className="auth-card"><b>localcode</b><p>Loading your cockpit…</p></div></main>;
  if (!supabase) return <main className="auth-screen"><div className="auth-card"><b>Connect Supabase</b><p>Add the project URL and publishable key to <code>web/.env</code>, then restart the app.</p></div></main>;
  if (!user) return <main className="auth-screen"><form className="auth-card" onSubmit={submit}><div className="auth-logo">N</div><h1>{mode === 'signin' ? 'Welcome back' : 'Create your cockpit'}</h1><p>Sign in to sync your DSA progress across devices.</p><label>Email<input type="email" required autoComplete="email" value={email} onChange={event => setEmail(event.target.value)} /></label><label>Password<input type="password" required minLength={6} autoComplete={mode === 'signin' ? 'current-password' : 'new-password'} value={password} onChange={event => setPassword(event.target.value)} /></label>{message && <div className="auth-message">{message}</div>}<button disabled={working}>{working ? 'Working…' : mode === 'signin' ? 'Sign in' : 'Create account'}</button><button className="auth-switch" type="button" onClick={() => { setMode(value => value === 'signin' ? 'signup' : 'signin'); setMessage(''); }}>{mode === 'signin' ? 'New here? Create an account' : 'Already have an account? Sign in'}</button></form></main>;
  return <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>;
}
