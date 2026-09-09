create table public.problem_progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  problem_id text not null,
  language text not null check (language in ('python', 'typescript')),
  completed boolean not null default true,
  completed_at timestamptz not null default now(),
  primary key (user_id, problem_id, language)
);

alter table public.problem_progress enable row level security;
revoke all on table public.problem_progress from anon, authenticated;
grant select, insert, update, delete on table public.problem_progress to authenticated;

create policy "Users read their own progress"
on public.problem_progress for select to authenticated
using ((select auth.uid()) = user_id);

create policy "Users insert their own progress"
on public.problem_progress for insert to authenticated
with check ((select auth.uid()) = user_id);

create policy "Users update their own progress"
on public.problem_progress for update to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create policy "Users delete their own progress"
on public.problem_progress for delete to authenticated
using ((select auth.uid()) = user_id);
