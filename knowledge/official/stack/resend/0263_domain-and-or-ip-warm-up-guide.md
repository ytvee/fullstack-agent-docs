# Domain and/or IP Warm-up Guide

Source: https://resend.com/docs/knowledge-base/warming-up

Learn how to warm up a domain or IP to avoid deliverability issues.

Warming up a domain or IP refers to the practice of progressively increasing your sending volume to maximize your deliverability. The goal is to send at a consistent rate and avoid any spikes in email volume that might be concerning to inbox service providers.

Whenever you change your sending patterns—whether because you're using a new domain, a new IP, or a new vendor, or because your volume will increase—you should warm-up your domain and/or IP.

A thought-out warm-up plan limits greylisting and delivery throttling, as well as helping establish a good domain and IP reputation.

As your volume increases, you'll need to monitor your bounce rate to ensure it remains below 4%, and your spam rate below 0.08%. An increase in these rates would be a sign that your warm-up plan needs to be slowed down and an investigation into the root causes of the increases started.

Following these rules and metrics will establish a good domain reputation.

<Info>
  Each sender has different constraints and needs, so these numbers are meant as
  a baseline. Our [Support team](https://resend.com/help) can work with you on
  devising a plan adapted to your needs.
</Info>

## Existing domain

If you're already sending from an existing domain with established reputation and volumes, you can use the following guidelines to start sending with Resend.


| **Day** | **Messages per day** | **Messages per hour** |
| ------- | -------------------- | --------------------- |
| **1**   | Up to 1,000 emails   | 100 Maximum           |
| **2**   | Up to 2,500 emails   | 300 Maximum           |
| **3**   | Up to 5,000 emails   | 600 Maximum           |
| **4**   | Up to 5,000 emails   | 800 Maximum           |
| **5**   | Up to 7,500 emails   | 1,000 Maximum         |
| **6**   | Up to 7,500 emails   | 1,500 Maximum         |
| **7**   | Up to 10,000 emails  | 2,000 Maximum         |

## New domain

Before you start sending emails with a brand new domain, it's especially important to have a warm-up plan so you can maximize your deliverability right from the start.


| **Day** | **Messages per day** | **Messages per hour** |
| ------- | -------------------- | --------------------- |
| **1**   | Up to 150 emails     |                       |
| **2**   | Up to 250 emails     |                       |
| **3**   | Up to 400 emails     |                       |
| **4**   | Up to 700 emails     | 50 Maximum            |
| **5**   | Up to 1,000 emails   | 75 Maximum            |
| **6**   | Up to 1,500 emails   | 100 Maximum           |
| **7**   | Up to 2,000 emails   | 150 Maximum           |

## Warm-up calculator

Use the calculator below to generate a personalized warm-up schedule based on your specific needs. Enter your target volume, timeline, and domain type to get a custom plan.

The guide is meant as a general plan, but always pay careful attention to your deliverability and adjust accordingly. If you have specific questions, [please reach out to us](https://resend.com/help).

<WarmupCalculator />

