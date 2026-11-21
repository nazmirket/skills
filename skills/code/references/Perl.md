# Perl

Check the supported Perl version, feature pragmas, CPAN dependencies, and how the script or module runs. Follow the project's Perl conventions and avoid requiring language features newer than its minimum.

- Prefer lexical scope and `strict` and `warnings` where compatible. Use names and explicit return values that make scalar, list, and void context unsurprising. Test both supported contexts if a public routine behaves differently in them. Distinguish `undef` from false values such as zero or an empty string.
- Keep parsing and policy separate from file or process I/O. Use lexical handles and three-argument `open`; check failures and choose encoding or raw bytes intentionally. Check close failures for output when they can signal a lost write. Use the argument-list form of process calls when invoking a command directly.
- Choose package exports deliberately. Prefer a small module interface and direct data structures; introduce an object when identity or lifecycle matters. For regular expressions that encode nontrivial rules, use named captures or documented groups and cover near misses.
- Stream large input line by line when practical and bound retained history. Watch repeated whole-file processing and nested regex backtracking on realistic long inputs. Profile a representative run before trading readability for compact syntax.

Use the project's tests and `perl -c` where relevant. Exercise bad input, zero-like values, encoding changes, and failed I/O as appropriate. Verify unchanged CLI exit codes and output when they are consumed by other programs.
