export default function Hero() {
  return (
    <section className="text-center mb-12">
      <img
        src={${import.meta.env.BASE_URL}Big.png}
        alt="Biblical Heritage Logo"
        width="400"
      />
      <h1 className="text-4xl font-bold mb-4">Biblical Heritage</h1>
      <p className="italic max-w-2xl mx-auto">
        “But sanctify the Lord God in your hearts: and be ready always to give
        an answer to every man that asketh you a reason of the hope that is in
        you with meekness and fear.”
      </p>
      <p className="mt-2">1 Peter 3:15 (KJV)</p>
    </section>
  );
}
