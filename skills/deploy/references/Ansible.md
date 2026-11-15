# Ansible

Confirm inventory, host pattern, collections and versions, connection strategy, privilege escalation, and the environment used to run the playbook. Check which variables and groups actually apply before targeting a batch.

- Prefer idempotent modules with explicit desired state. If using a command, define when it changes state and how failures must surface. Notify a handler only on real changes; verify ordering if a subsequent check needs the handler's effects before the play ends.
- Use syntax and inventory checks, then check mode and diff where the modules support them. Check mode may skip operations or be unable to model a later task that depends on dynamic state; rehearse on a representative host. Protect sensitive task output and diffs, not just secret files in Git.
- Roll out with scoped host batches when the task can remove capacity or interrupt traffic. Tie batch size to service redundancy. Check long-lived connections and drain or remove targets through the established service process only when authorized.
- Break down time into gathering facts, connection setup, remote work and retries. Limit fact gathering where safe; consider connection reuse, pipelining and forks only after checking privilege policy and remote capacity. Keep constrained services protected from bursts.

Verify a user path after the first batch before widening exposure. Recheck idempotence when safe. Plan the actual recovery config or artifact; rerunning an old playbook does not automatically restore files or data it didn't manage.

Upstream: [Check and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html), [Execution strategies and batches](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_strategies.html), [Handlers](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html).
