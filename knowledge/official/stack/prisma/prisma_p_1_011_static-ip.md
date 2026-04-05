# Static IP (/docs/accelerate/static-ip)



You can enable static IP for Accelerate when your security setup requires IP allowlisting or if you're implementing firewalls that only permit access from trusted IPs, ensuring controlled and secure database connections.

<img alt="Result of enabling static IP Accelerate with a database using IP allowlisting" src="/img/accelerate/result-of-adding-static-ip-to-accelerate.png" width="2960" height="1406" />

<CalloutContainer type="info">
  <CalloutDescription>
    To enable static IP support for Accelerate within an existing or a new project environment, your workspace will need to be on our Pro or Business plans. Take a look at the [pricing page](https://www.prisma.io/pricing#accelerate) for more information.
  </CalloutDescription>
</CalloutContainer>

Enable static IP in Accelerate [#enable-static-ip-in-accelerate]

You can opt-in to use static IP for Accelerate in the [Platform Console](https://pris.ly/pdp) in two ways:

1. When enabling Accelerate for your project environment: [#1-when-enabling-accelerate-for-your-project-environment]

1. Specify your database connection string and connection pool region.
2. Enable static IP by toggling the **Static IP** switch in the **Network restrictions** section.
3. Click on the **Enable Accelerate** button.

2. For projects already using Accelerate: [#2-for-projects-already-using-accelerate]

1. Navigate to the Accelerate **Settings** tab in the project environment.
2. Enable static IP by toggling the **Static IP** switch in the **Network restrictions** section.

Enabling static IP for Accelerate will provide you with a list of static IPv4 and IPv6 addresses.

Once you have these addresses, configure your database firewall to allow incoming connections only from these IPs and any other trusted IPs that need access to your database.

<CalloutContainer type="info">
  <CalloutDescription>
    Since you cannot enable static IP for an existing Accelerate-enabled environment, we recommend opting for static IP when enabling Accelerate in a new environment. Use the same database URL as your existing Accelerate environment to instantly access static IP support for Accelerate.
  </CalloutDescription>
</CalloutContainer>


