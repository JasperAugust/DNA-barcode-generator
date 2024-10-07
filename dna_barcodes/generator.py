import random
import subprocess


class BarcodesGenerator:
    def __init__(
        self,
        desired_gc_content=0.50,
        gc_tolerance=0.10,
        sequence_length=16,
        number_of_sequences=64,
        min_dissimilarity=0.15,
    ):
        self.desired_gc_content = desired_gc_content
        self.gc_tolerance = gc_tolerance
        self.sequence_length = sequence_length
        self.number_of_sequences = number_of_sequences
        self.min_dissimilarity = min_dissimilarity
        self.max_similarity = (1 - min_dissimilarity) * sequence_length

    def generate_sequence(self):
        gc_count = int(self.sequence_length * self.desired_gc_content)
        at_count = self.sequence_length - gc_count
        sequence_list = (
            ["G"] * (gc_count // 2)
            + ["C"] * (gc_count - gc_count // 2)
            + ["A"] * (at_count // 2)
            + ["T"] * (at_count - at_count // 2)
        )
        random.shuffle(sequence_list)
        return "".join(sequence_list)

    @staticmethod
    def hamming_distance(seq1, seq2):
        return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

    def local_blast_sequence(self, sequence):
        with open("temp_seq.fasta", "w") as f:
            f.write(">Query\n" + sequence + "\n")
        result = subprocess.run(
            [
                "blastn",
                "-task",
                "blastn-short",
                "-query",
                "temp_seq.fasta",
                "-db",
                "combined_genomes_db",
                "-outfmt",
                "6",
                "-evalue",
                "1",
            ],
            stdout=subprocess.PIPE,
        )
        output = result.stdout.decode("utf-8")
        return bool(output.strip())

    def generate_barcodes(self):
        unique_sequences = []
        generated_sequences = set()
        max_attempts = 100000
        attempts = 0

        while (
            len(unique_sequences) < self.number_of_sequences and attempts < max_attempts
        ):
            seq = self.generate_sequence()
            attempts += 1

            if seq in generated_sequences:
                continue
            generated_sequences.add(seq)

            gc_count = seq.count("G") + seq.count("C")
            gc_fraction = gc_count / self.sequence_length
            if abs(gc_fraction - self.desired_gc_content) > self.gc_tolerance:
                continue

            is_similar = any(
                self.hamming_distance(seq, existing_seq)
                < (self.sequence_length - self.max_similarity)
                for existing_seq in unique_sequences
            )
            if is_similar:
                continue

            if self.local_blast_sequence(seq):
                continue

            unique_sequences.append(seq)
            print(f"Sequence {len(unique_sequences)}: {seq}")

        if len(unique_sequences) < self.number_of_sequences:
            print(
                f"Only {len(unique_sequences)} sequences were generated after {attempts} attempts."
            )
        else:
            print("Successfully generated all sequences.")

        return unique_sequences

    def save_sequences(self, sequences, filename="unique_sequences.txt"):
        with open(filename, "w") as f:
            for seq in sequences:
                f.write(seq + "\n")
