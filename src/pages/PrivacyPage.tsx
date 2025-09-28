import SecondaryLayout from "../components/SecondaryLayout";

export default function PrivacyPage() {
  return (
    <SecondaryLayout>
      <h1 className="text-3xl font-bold mb-6">Privacy Policy</h1>
      <p className="text-lg text-verse leading-relaxed">
        This app respects your privacy and intellectual property. We do not collect personal data
        or track usage without consent. All content is protected under applicable copyright laws.
      </p>
    </SecondaryLayout>
  );
}