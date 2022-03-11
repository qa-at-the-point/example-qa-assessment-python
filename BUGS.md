# Overview

- HTML does not follow A11y best practices and guidelines
- Veriff Me works even when no config values are set

## Accessibility (A11y)

Although A11y was originally "out of scope", as I was exploring the DOM for UI Automation,
the dropdowns and their options where in different places and also not following "best practice"
of using a `<select>` element which has A11y functionality built-in.

### Steps

1. Open Veriff website
2. Inspect any of the dropdown elements (ie language or country)
3. Observe that their options are located in a completely different location in the DOM

### Risks

This does not affect functionality for an abled person, but this would be _unusable_ for anyone using a **screen reader** or navigating with their keyboard.

### Solutions

I could further test this using manual and automated tools including Lighthouse and aXe. This would provide an audit and actionable report for the team to resolve.

## No Error Flows

Leaving fields and values blank/missing does not raise any errors to the user. This was especially confusing because Veriff behaved as if _everything was fine_!

### Steps

1. Open Veriff website
2. Click `Veriff Me` button
3. Veriff flow starts with no problems

### Risks

Defaults are sent when this happens, but I don't think that's the best experience for the user. It was confusing for things to default to a random person's name with a country and language I didn't select.

### Solutions

Instead, I would rather the missing fields highlight in red to visually show they are missing and need to be selected by the user. This "call to action" would prevent a lot of headache for the user - not to mention save our engineering team extra logs, traces, etc. that are not as useful.
