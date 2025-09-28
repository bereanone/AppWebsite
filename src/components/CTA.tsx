export default function CTA() {
  return (
    <section className="bg-sand text-sepia font-cambria py-20">
      <div className="max-w-4xl mx-auto px-6">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-6">
          Ready to Explore Biblical Heritage?
        </h2>
        <p className="text-lg text-verse mb-8 leading-relaxed text-left">
          Join us on the journey to build a study tool that blends history,
          theology, and accessibility.
        </p>
        <a
          href="#contact"
          className="inline-block bg-accent text-sepia font-semibold px-6 py-3 rounded hover:bg-accentHover transition"
        >
          Get Involved
        </a>
      </div>
    </section>
  );
}