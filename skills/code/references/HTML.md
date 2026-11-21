# HTML

Use document structure and native behavior before custom roles or script. Match the browser support target and the product's content semantics.

- Make heading order reflect the content and use landmarks where they help navigation. Use links for navigation and buttons for actions. Avoid nesting interactive elements. Be explicit about button types in forms that have non-submit actions.
- Associate controls with visible labels. Group related choices, identify required or invalid input with text, and associate help and error messages programmatically. Preserve user input and make recovery clear. Client constraints support the experience; validate at the server boundary too.
- Make source and focus order meaningful without CSS. Add useful alternatives for informative images and empty alternatives for decorative images. Use range-appropriate image sources or dimensions when they improve load and reduce layout shift.
- Use progressive enhancement when a native path can preserve the task. For custom behavior, test keyboard input, status feedback, and relevant touch or assistive technology. Do not infer accessible behavior from visual markup or a passing validator alone.

## Preserve browser behavior

- Check the actual form data contract: which controls have names, submitter behavior, disabled fields, and unchecked or repeated inputs. Choose autocomplete and input types by meaning; preserve user-entered values on recoverable failure.
- Make the image sizing and loading decision by role. Reserve dimensions where possible; avoid deferring the principal above-the-fold image without evidence. For responsive sources, verify that the browser selects a sensible asset at representative viewports and pixel densities.
- For templates or dynamic markup, inspect the parsed DOM. The browser may repair invalid nesting differently from the apparent source tree, affecting hydration, focus and accessibility. Use the existing route or template tests as well as validation where appropriate.

Inspect parsed DOM and accessibility tree, and exercise form submission and errors using keyboard alone. Check the real route and language when templates or rendering alter actual output.
