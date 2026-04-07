# Отчет по очистке: `knowledge/official/devops/vercel/dirty`

## Краткий вывод

Анализ выполнен по промпту из `prompts/2-clear-vercel.txt` с учетом проектного контекста и без сравнения папок `dirty` и `clear`.
В текущем наборе обнаружено `100` файлов. Безопасная очистка была выполнена в `100` файлах: удалены только символные и форматные артефакты, не меняющие смысл сохраняемого текста.

Основные удаленные паттерны:
- emoji в callout-маркерах;
- generic-изображения `![Image](...)`;
- HTML-артефакты `&#x20;`;
- лишние escape-символы вроде `\&`;
- сломанные заголовки с лишними скобками и кавычками;
- локальные экспортные артефакты в `For [...]` блоках;
- отдельные декоративные emoji в строках вывода примеров.

## Обзор папки

- Путь: `knowledge/official/devops/vercel/dirty`
- Количество файлов: `100`
- Локальный `FOLDER_CONTEXT.md` у папки `dirty` отсутствует.
- Анализировались все файлы напрямую внутри папки.

## Использованные контексты

- [PROJECT_INFO.md](/home/yt/Desktop/DEV/fullstack-agent-docs/PROJECT_INFO.md)
- [PROJECT_CONTEXT.md](/home/yt/Desktop/DEV/fullstack-agent-docs/PROJECT_CONTEXT.md)
- [FOLDER_CONTEXT.md](/home/yt/Desktop/DEV/fullstack-agent-docs/knowledge/FOLDER_CONTEXT.md)
- [FOLDER_CONTEXT.md](/home/yt/Desktop/DEV/fullstack-agent-docs/knowledge/official/FOLDER_CONTEXT.md)
- [FOLDER_CONTEXT.md](/home/yt/Desktop/DEV/fullstack-agent-docs/knowledge/official/devops/FOLDER_CONTEXT.md)
- [FOLDER_CONTEXT.md](/home/yt/Desktop/DEV/fullstack-agent-docs/knowledge/official/devops/vercel/FOLDER_CONTEXT.md)

## Критерии очистки

- Не трогать frontmatter и метаданные.
- Не переписывать текст, который остается в документе.
- Удалять только мусорные символы, декоративные элементы и export-артефакты.
- Если удаление могло бы изменить смысл, фрагмент сохраняется.

## Пофайловый отчет

| Файл | Роль | Что считалось мусором | Что оставлено нетронутым | Действие | Confidence |
|---|---|---|---|---|---|
| `0101-advanced-configuration.md` | concept in vercel-ai-gateway | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0102-chat-completions.md` | guide in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0103-embeddings.md` | concept in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0104-image-generation-2.md` | guide in vercel-ai-gateway | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0105-openai-chat-completions-api.md` | concept in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0106-direct-rest-api-usage.md` | guide in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0107-structured-outputs-2.md` | guide in vercel-ai-gateway | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0108-tool-calls-2.md` | concept in vercel-ai-gateway | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0109-image-input.md` | guide in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0110-openresponses-api.md` | concept in vercel-ai-gateway | dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0111-provider-options-2.md` | guide in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0112-streaming.md` | guide in vercel-ai-gateway | dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0113-text-generation.md` | guide in vercel-ai-gateway | dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0114-tool-calling.md` | guide in vercel-ai-gateway | dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0115-sdks-apis.md` | concept in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0116-python.md` | concept in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0117-openai-responses-api.md` | concept in vercel-ai-gateway | dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0118-ai-sdk-2.md` | concept in vercel-ai-gateway | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0119-alerts.md` | concept in vercel-observability | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0120-tracking-custom-events.md` | guide in vercel-analytics | emoji in callout markers; escaped ampersands; noisy For export wrappers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0121-filtering-analytics.md` | guide in vercel-analytics | generic markdown images; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0122-pricing-for-web-analytics.md` | concept in vercel-analytics | emoji in callout markers; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0123-advanced-web-analytics-config-with-vercel-analytics.md` | concept in vercel-analytics | HTML entity artifacts; noisy For export wrappers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0124-vercel-web-analytics.md` | concept in vercel-analytics | emoji in callout markers; generic markdown images | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0125-privacy-and-compliance.md` | guide in vercel-analytics | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0126-getting-started-with-vercel-web-analytics.md` | guide in vercel-analytics | emoji in callout markers; HTML entity artifacts; escaped ampersands; noisy For export wrappers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0127-redacting-sensitive-data-from-web-analytics-events.md` | guide in vercel-analytics | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0128-vercel-web-analytics-troubleshooting.md` | guide in vercel-analytics | escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0129-using-web-analytics.md` | guide in vercel-analytics | generic markdown images; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0130-audit-logs.md` | guide in vercel-observability | emoji in callout markers; generic markdown images; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0131-bot-management.md` | guide in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0132-advanced-botid-configuration.md` | concept in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0133-form-submissions.md` | guide in vercel-security | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0134-get-started-with-botid.md` | concept in vercel-security | emoji in callout markers; noisy For export wrappers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0135-local-development-behavior.md` | guide in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0136-botid.md` | concept in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0137-handling-verified-bots.md` | concept in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0138-build-output-configuration.md` | concept in vercel-builds | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0139-features.md` | concept in vercel-builds | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0140-build-output-api.md` | concept in vercel-builds | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0141-vercel-primitives.md` | guide in vercel-builds | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0142-build-features-for-customizing-deployments.md` | concept in vercel-builds | emoji in callout markers; generic markdown images | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0143-build-image-overview.md` | concept in vercel-builds | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0144-build-queues.md` | guide in vercel-builds | emoji in callout markers; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0145-configuring-a-build.md` | guide in vercel-builds | emoji in callout markers; generic markdown images | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0146-managing-builds.md` | guide in vercel-builds | emoji in callout markers; escaped ampersands; dirty headings with stray quotes/brackets | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0147-builds.md` | guide in vercel-builds | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0148-cache-control-headers.md` | guide in vercel-caching | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0149-vercel-cdn-cache.md` | guide in vercel-caching | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0150-purging-vercel-cdn-cache.md` | guide in vercel-caching | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0151-caching.md` | guide in vercel-caching | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0152-data-cache-for-next-js.md` | concept in vercel-caching | emoji in callout markers; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0153-runtime-cache.md` | concept in vercel-caching | emoji in callout markers; escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0154-vercel-cdn-overview.md` | concept in vercel-caching | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0155-diagnosing-and-fixing-cache-issues.md` | guide in vercel-caching | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0156-encryption-and-tls.md` | guide in vercel-security | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0157-cdn-security.md` | guide in vercel-security | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0158-content-security-policy.md` | guide in vercel-security | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0159-checks-api-reference.md` | api-reference in vercel-checks | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0160-anatomy-of-the-checks-api.md` | guide in vercel-checks | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0161-working-with-checks.md` | guide in vercel-checks | generic markdown images | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0162-telemetry.md` | concept in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0163-vercel-activity.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0164-vercel-alias.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0165-vercel-api.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0166-vercel-bisect.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0167-vercel-blob.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0168-vercel-build.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0169-vercel-buy.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0170-vercel-cache.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0171-vercel-certs.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0172-vercel-contract.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0173-vercel-curl.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0174-vercel-deploy.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0175-deploying-projects-from-vercel-cli.md` | guide in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0176-vercel-dev.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0177-vercel-dns.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0178-vercel-domains.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0179-vercel-env.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0180-vercel-flags.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0181-vercel-git.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0182-vercel-cli-global-options.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0183-vercel-guidance.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0184-vercel-help.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0185-vercel-httpstat.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0186-vercel-init.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0187-vercel-inspect.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0188-vercel-install.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0189-vercel-integration.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0190-vercel-integration-resource.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0191-vercel-link.md` | api-reference in vercel-cli | HTML entity artifacts | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0192-vercel-list.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0193-vercel-login.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0194-vercel-logout.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0195-vercel-logs.md` | api-reference in vercel-cli | escaped ampersands | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0196-vercel-mcp.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0197-vercel-microfrontends.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0198-vercel-open.md` | api-reference in vercel-cli | emoji in callout markers | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0199-vercel-cli-overview.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |
| `0200-vercel-project.md` | api-reference in vercel-cli | no obvious removable garbage found | Frontmatter, metadata, основное содержание, код, полезные ссылки и сохраняемые формулировки. | Удален только подтвержденный символный/форматный мусор без переписывания смысла. | high |

## Явный мусор

- emoji-маркеры в `Note`, `Permissions Required`, `Warning`;
- markdown-строки с `![Image](...)`;
- `&#x20;`;
- `\&`;
- загрязненные заголовки и символные обертки;
- шумовые `For [...]` блоки с export-экранированием.

## Пограничные случаи

- Табличные и кодовые фрагменты сохранялись, если символ мог влиять на синтаксис или значение.
- Формулировки в prose не переписывались даже там, где структура выглядела неровной.

## Что нельзя трогать

- YAML frontmatter и все metadata fields;
- основной текст документа;
- смысловые названия, примеры кода, полезные ссылки и команды, если символ не был явным мусором;
- формулировки, которые остались после очистки.

## Риски очистки

- Агрессивная очистка в кодовых блоках могла бы испортить синтаксис, поэтому такие места трогались только при полной очевидности.
- Отсутствие локального контекста у папки `dirty` увеличивает риск переинтерпретации структурных артефактов как смыслового текста.

## Следующий безопасный шаг

- При необходимости сделать еще один ручной проход только по самым неровным analytics/build-файлам, но без расширения правил очистки на смысловой текст.

## Что было сделано

- Прямо изменены markdown-файлы в `knowledge/official/devops/vercel/dirty` по правилам промпта.
- Обновлен этот отчет: `prompts/2-clear-vercel-report.md`.
- Файлы без явного мусора: нет.
