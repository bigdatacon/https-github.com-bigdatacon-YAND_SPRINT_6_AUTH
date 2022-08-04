import sentry_sdk
sentry_sdk.init(
    dsn="https://b2acd0589f6e4806b3d5b91268ffaab9@o1346398.ingest.sentry.io/6624269",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0