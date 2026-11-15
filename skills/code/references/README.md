# Stack guides

Pick the guide that owns the question. File extensions and imports are clues; confirm the renderer, framework, runtime, or database in use. The base language and framework guides answer different questions; one guide often suffices. Use upstream references for the project's versions.

| Area | Start here |
| --- | --- |
| JavaScript and TypeScript | [TypeScript (TS)](TypeScript.md), [JavaScript (JS)](JavaScript.md), [JSX / TSX](JSX.md) |
| UI and web frameworks | [Vue](Vue.md), [Angular](Angular.md), [React](React.md), [Next.js](Next.md), [Nuxt](Nuxt.md) |
| Web platform and styling | [HTML](HTML.md), [CSS](CSS.md), [Tailwind CSS](Tailwind.md), [Node.js](Node.md) |
| Relational data | [SQL](SQL.md), [PostgreSQL](PostgreSQL.md), [SQL Server / T-SQL](SQLServer.md) |
| Applications and systems | [Python](Python.md), [Go](Go.md), [Rust](Rust.md), [C++](Cpp.md), [C#](CSharp.md), [Swift](Swift.md), [Java](Java.md), [Kotlin](Kotlin.md) |
| Dart and mobile UI | [Dart](Dart.md), [Flutter](Flutter.md) |
| PHP applications | [PHP](PHP.md), [Laravel](Laravel.md) |
| Data analysis and scripting | [R / RLang](R.md), [Perl](Perl.md), [Bash](Bash.md) |
| C and Apple interoperability | [C](C.md), [Objective-C](ObjectiveC.md) |

[Engineering Practices](EngineeringPractices.md) covers decisions that are the same across stacks.

- For JSX markup, TSX prop types, or transform errors, start with JSX / TSX. For React state or effects, use React; for Next.js caching or server boundaries, use Next.js. A `.tsx` file does not imply React.
- For result semantics, joins, aggregation, or query shape, use SQL. For planner, migration, or concurrency behavior specific to a database, start with the engine guide or that engine's upstream docs.
- For widget state or frame performance, use Flutter. For a language or library question outside the widget layer, use Dart. Treat PHP and Laravel, Vue and Nuxt, and CSS and Tailwind the same way: add the second guide when its rules govern part of the change.
