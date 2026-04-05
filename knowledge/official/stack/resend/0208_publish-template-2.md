# Publish template
curl -X POST 'https://api.resend.com/templates/{template_id}/publish' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json'
```
</CodeGroup>

After you publish a template, you can freely work on it through the editor or [via the API](/api-reference/templates/update-template) without affecting the published version. This allows you to test and validate new edits before sending them to users.

## Version History

As you work on a Template, your changes are saved as a draft, although you can also manually save drafts by pressing <kbd>Cmd</kbd> + <kbd>S</kbd> (Mac) or <kbd>Ctrl</kbd> + <kbd>S</kbd> (Windows). Only after publishing again will the changes be reflected in emails using the Template.

Each template contains a version history that helps you track changes your team has made over time. You can view the version history by clicking the three dots in the top right corner of the template editor and selecting **Version History**.

Through the version history, you can preview each version, who made them, and when they were made. You can also revert to a previous version if needed.

<video />

Reverting creates a new draft based on the selected version's content, without affecting the published template.

## Iterating on a template

You can work on a new draft version of your published template, update the design and messaging, then test it thoroughly before publishing it again. Your email sending will continue to use the current published version until you're ready to make the switch, without the need to create a new separate template or risk leaking your new logo.

This behavior is also useful to avoid breaking changes when you need to edit a template that's in production. Add or remove variables, update the design, and more without affecting your existing emails or raising validation errors.

