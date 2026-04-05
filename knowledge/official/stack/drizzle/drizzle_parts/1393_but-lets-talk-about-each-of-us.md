#### But let's talk about each of us:

<style>{`
  .team-member {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .team-member__info {
    flex: 0 0 50%;
    max-width: 50%;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .team-member__name {
    margin-top: 0 !important;
    margin-bottom: 0.75rem;
  }

  .team-member__photo {
    width: 100%;
    max-width: 50%;
    flex: 0 0 50%;
    border-radius: 12px;
  }

  @media (max-width: 900px) {
    .team-member {
      flex-direction: column-reverse;
      gap: 1rem;
    }

    .team-member__photo {
      width: 100%;
      max-width: 320px;
      flex: 0 0 auto;
      align-self: center;
    }

    .team-member__info {
      max-width: 100%;
      flex: 0 0 auto;
    }
  }
`}</style>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Oleksandr Blokh (Alex)</h4>
    <p>
      Alex co-created Drizzle and helped start the Drizzle team. He's been here
      since 2021, when the first code was written for <code>drizzle-orm</code>.
    </p>
    <p>
      Now he leads core Drizzle development and works on Drizzle Studio,
      OneDollarStats, RubberBoots, and other projects.
    </p>
    <p>
      Give him a sub <a href="https://x.com/_alexblokh">on X</a> •{" "}
      <a href="https://github.com/AlexBlokh">GitHub</a>
    </p>
  </div>
  <Image
    class="team-member__photo"
    src={blokh}
    alt="Oleksandr Blokh"
    width={400}
  />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Andrii Sherman (Andrew)</h4>
    <p>
      Andrew is another Drizzle co-creator and co-founder. Back in 2020, he
      wrote a Drizzle ORM in Java. Later, seeing the need for the same kind of
      tool in the TypeScript world, he and Alex pivoted it to TypeScript. That's
      where it all started.
    </p>
    <p>
      Give him a sub <a href="https://x.com/andrii_sherman">on X</a> •{" "}
      <a href="https://github.com/AndriiSherman">GitHub</a>
    </p>
  </div>
  <Image
    class="team-member__photo"
    src={andrew}
    alt="Andrii Sherman"
    width={400}
  />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Dan Kochetov</h4>
    <p>
      Dan was the first to take on a full <code>drizzle-orm</code> rewrite and
      turn it into the API you know today. He also created the first version of
      Relational Queries.
    </p>
    <p>
      Now, after a short break, Dan is back in action and ready to ship more
      great things for Drizzle.
    </p>
    <p>
      Give him a sub <a href="https://x.com/bloberenober">on X</a> •{" "}
      <a href="https://github.com/dankochetov">GitHub</a>
    </p>
  </div>
  <Image class="team-member__photo" src={dan} alt="Dan Kochetov" width={400} />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Roman Nabukhotnyi (Zeus)</h4>
    <p>
      Roman (Zeus) is working hard to bring Drizzle Studio to you in every
      possible form.
    </p>
    <p>
      Roman is writing a lot about Drizzle Studio{" "}
      <a href="https://x.com/nabukhotnyi">on X</a> •
      <a href="https://github.com/RomanNabukhotnyi">GitHub</a>
    </p>
  </div>
  <Image
    class="team-member__photo"
    src={roman}
    alt="Roman Nabukhontyi"
    width={400}
  />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Serhii Reka</h4>
    <p>
      Serhii rewrote Relational Queries, mastered TypeScript types at the
      highest level, and continues shipping great features to the{" "}
      <code>drizzle</code> ecosystem.
    </p>
    <p>
      Give him a sub <a href="https://x.com/s_reka_">on X</a> •{" "}
      <a href="https://github.com/Sukairo-02">GitHub</a>
    </p>
  </div>
  <Image class="team-member__photo" src={reka} alt="Serhii Reka" width={400} />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">Oleksandr Sherman</h4>
    <p>
      Oleksandr ("Sania") is a <code>drizzle-kit</code> wizard. He helped
      rewrite the
      <code>alternation-engine</code>, the drizzle-kit test suite, and is now on
      a mission to make sure there are 0 GitHub issues left with the{" "}
      <code>drizzle-kit</code> tag.
    </p>
    <p>
      Give him a sub <a href="https://x.com/_alex_sherman">on X</a> •{" "}
      <a href="https://github.com/AleksandrSherman">GitHub</a>
    </p>
  </div>
  <Image
    class="team-member__photo"
    src={alex_sherman}
    alt="Oleksandr Sherman"
    width={400}
  />
</section>

<section class="team-member">
  <div class="team-member__info">
    <h4 class="team-member__name">SMM Manager</h4>
    <p>
      "I'm now professionally responsible for what used to happen on X for free"
      (c)
    </p>
    <p>
      Give him a sub: <a href="https://x.com/DrizzleOrm">X</a>
    </p>
  </div>
  <Image class="team-member__photo" src={smm} alt="SMM Manager" width={400} />
</section>

