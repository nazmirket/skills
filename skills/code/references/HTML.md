# HTML

Use document structure and native behavior before custom roles or script. Match the browser support target and the product's content semantics.

- Make heading order reflect the content and use landmarks where they help navigation. Use links for navigation and buttons for actions. Avoid nesting interactive elements. Be explicit about button types in forms that have non-submit actions.
- Associate controls with visible labels. Group related choices, identify required or invalid input with text, and associate help and error messages programmatically. Preserve user input and make recovery clear. Client constraints support the experience; validate at the server boundary too.
- Make source and focus order meaningful without CSS. Add useful alternatives for informative images and empty alternatives for decorative images. Use range-appropriate image sources or dimensions when they improve load and reduce layout shift.
- Use progressive enhancement when a native path can preserve the task. For custom behavior, test keyboard input, status feedback, and relevant touch or assistive technology. Do not infer accessible behavior from visual markup or a passing validator alone.

Inspect parsed DOM and accessibility tree, and exercise form submission and errors using keyboard alone. Check the real route and language when templates or rendering alter actual output.

Standards: [HTML forms](https://html.spec.whatwg.org/multipage/forms.html), [W3C WAI forms tutorial](https://www.w3.org/WAI/tutorials/forms/).
